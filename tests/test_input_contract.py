import json
import tempfile
import unittest
from pathlib import Path
from src.forecast_reader import load


class InputContractTests(unittest.TestCase):
    def test_primary_material_is_readable(self):
        self.assertGreater(len(load(Path(__file__).resolve().parents[1] / 'fixtures/counts.csv')), 0)

    def test_all_materials_can_be_read(self):
        root = Path(__file__).resolve().parents[1] / "fixtures"
        files = sorted(p for p in root.rglob("*") if p.suffix in (".csv", ".json", ".jsonl"))
        self.assertTrue(files)
        for path in files:
            with self.subTest(path=path.name):
                self.assertIsInstance(load(path), (list, dict))

    def test_missing_is_not_zero(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.csv"
            path.write_text("id,value\na,\nb,0\n", encoding="utf-8")
            rows = load(path)
            self.assertEqual(rows[0]["value"], "")
            self.assertEqual(rows[1]["value"], "0")

    def test_invalid_json_stops_reading(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.jsonl"
            path.write_text('{"key":1}\n{bad}\n', encoding="utf-8")
            with self.assertRaises(json.JSONDecodeError):
                load(path)

    def test_missing_file_does_not_become_empty_material(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(FileNotFoundError):
                load(Path(directory) / "absent.csv")
