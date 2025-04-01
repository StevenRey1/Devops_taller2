import unittest
from functions import load_file

class TestFunctions(unittest.TestCase):

    def test_load_file(self):
        # Archivo de prueba
        test_data = "test_heroes.csv"
        
        # Crear un archivo de prueba con datos simulados
        with open(test_data, "w") as f:
            f.write("id;name;gender;eye_color;race;hair_color;height;publisher;skin_color;alignment;weight\n")
            f.write("1;Superman;Male;Blue;Kryptonian;Black;191;DC Comics;None;Good;101\n")
        
        heroes = load_file(test_data)
        
        # Verificar que se haya cargado correctamente
        self.assertIn("1", heroes)
        self.assertEqual(heroes["1"]["name"], "Superman")
        self.assertEqual(heroes["1"]["publisher"], "DC Comics")

if __name__ == '__main__':
    unittest.main()
