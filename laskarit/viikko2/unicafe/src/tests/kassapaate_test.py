import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()

    def test_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassa, None)

    def test_oikea_maara(self):
        self.assertEqual(self.kassa.kassassa_rahaa,100000)
        self.assertEqual(self.kassa.edulliset,0)
        self.assertEqual(self.kassa.maukkaat,0)

    def test_kateinen_edullinen(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(250),10)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000+240)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_kateinen_maukas(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(500),100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000+400)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_kateinen_edullinen_ei_riittava(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(200),200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_kateinen_maukas_ei_riittava(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(200),200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_kortti_edullinen_True(self):
        kortti = Maksukortti(1000)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(kortti), True)
        self.assertEqual(kortti.saldo, 1000-240)
        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kortti_edullinen_False(self):
        kortti = Maksukortti(230)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(kortti), False)
        self.assertEqual(kortti.saldo, 230)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kortti_maukas_True(self):
        kortti = Maksukortti(1000)
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(kortti), True)
        self.assertEqual(kortti.saldo, 1000-400)
        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kortti_maukas_False(self):
        kortti = Maksukortti(230)
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(kortti), False)
        self.assertEqual(kortti.saldo, 230)
        self.assertEqual(self.kassa.maukkaat, 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_lataus(self):
        kortti = Maksukortti(250)
        self.kassa.lataa_rahaa_kortille(kortti, 250)
        self.assertEqual(kortti.saldo, 500)
