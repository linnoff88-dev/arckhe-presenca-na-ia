"""Testes do kit Presença na IA: python3 -m unittest discover -s tests"""
import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

RAIZ = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "kit"))
import diagnostico as d  # noqa: E402

EMP = {"nome": "Padaria Sol", "apelidos": ["Sol Pães"], "cidade": "Curitiba", "servico": "padaria",
       "site": "https://www.padariasol.com.br/", "concorrentes": ["Pão Dourado"], "confunde_com": ["Hotel Sol"]}


class TestMarcar(unittest.TestCase):
    def test_resposta_perfeita_vale_100(self):
        m = d.marcar(EMP, "A Padaria Sol (padariasol.com.br) é ótima.")
        self.assertEqual(m["nota"], 100)

    def test_ausente_sem_site_vale_30(self):
        self.assertEqual(d.marcar(EMP, "Não conheço.")["nota"], 30)

    def test_confusao_e_concorrente_tiram_pontos(self):
        m = d.marcar(EMP, "Você quis dizer o Hotel Sol? Recomendo o Pão Dourado.")
        self.assertEqual(m["confusao"], ["Hotel Sol"])
        self.assertEqual(m["concorrentes"], ["Pão Dourado"])
        self.assertEqual(m["nota"], 0)

    def test_acento_e_caixa_nao_importam(self):
        self.assertTrue(d.marcar(EMP, "sol paes fica no centro")["aparece"])

    def test_marca_trocada_nao_conta_como_aparece(self):
        m = d.marcar(EMP, "A Padaria Sol? Você quis dizer o Hotel Sol, no centro.")
        self.assertFalse(m["aparece"])
        self.assertEqual(m["nota"], 10)

    def test_palavra_inteira(self):
        emp = dict(EMP, nome="INEMA", apelidos=[])
        self.assertFalse(d.marcar(emp, "O melhor cinema da cidade.")["aparece"])

    def test_dominio_sem_www_e_barra(self):
        self.assertEqual(d.dominio("https://www.padariasol.com.br/loja"), "padariasol.com.br")


class TestCli(unittest.TestCase):
    def rodar(self, *args):
        return subprocess.run([sys.executable, str(RAIZ / "kit" / "diagnostico.py"), *args],
                              capture_output=True, text=True)

    def test_perguntas_trocam_nomes(self):
        r = self.rodar("perguntas", str(RAIZ / "kit" / "exemplo-empresa.json"))
        self.assertEqual(r.returncode, 0)
        self.assertIn("O que você sabe da empresa INEMA?", r.stdout)
        self.assertEqual(r.stdout.count("\n"), 4)

    def test_relatorio_antes_e_depois_do_exemplo(self):
        emp = str(RAIZ / "kit" / "exemplo-empresa.json")
        antes = self.rodar("relatorio", emp, str(RAIZ / "kit" / "exemplo-respostas-antes.json"))
        depois = self.rodar("relatorio", emp, str(RAIZ / "kit" / "exemplo-respostas-depois.json"))
        self.assertEqual((antes.returncode, depois.returncode), (0, 0))
        self.assertNotIn("_nota", antes.stdout)
        self.assertIn("Instituto do Meio Ambiente", antes.stdout)
        self.assertIn("Nota geral: 20/100", antes.stdout)
        self.assertIn("aparece em 0 de 1", antes.stdout)
        self.assertIn("Nota geral: 100/100", depois.stdout)

    def test_json_sem_campo_sai_2(self):
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
            json.dump({"nome": "X"}, f)
        r = self.rodar("perguntas", f.name)
        self.assertEqual(r.returncode, 2)
        self.assertIn("sem 'cidade'", r.stderr)

    def test_respostas_vazias_sai_2(self):
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
            json.dump({}, f)
        r = self.rodar("relatorio", str(RAIZ / "kit" / "exemplo-empresa.json"), f.name)
        self.assertEqual(r.returncode, 2)

    def test_saida_grava_arquivo(self):
        with tempfile.TemporaryDirectory() as t:
            alvo = pathlib.Path(t) / "rel.md"
            r = self.rodar("relatorio", str(RAIZ / "kit" / "exemplo-empresa.json"),
                           str(RAIZ / "kit" / "exemplo-respostas-antes.json"), "--saida", str(alvo))
            self.assertEqual(r.returncode, 0)
            self.assertTrue(alvo.read_text(encoding="utf-8").startswith("# Diagnóstico"))


if __name__ == "__main__":
    unittest.main()
