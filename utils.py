import json, re

def get_stringz_full(filepath: str) -> tuple[list[str], list[str]]:
	with open(filepath, 'r', encoding='utf-8', errors='ignore') as stringz_full:
		stringz_offsets = []
		stringz_lines = []
		for line in stringz_full:
			line = line[:-1]
			if line.startswith('_' * 80):
				stringz_offsets.append(line)
				stringz_lines.append(None)
			elif stringz_lines[-1] is None:
				stringz_lines[-1] = line
			else:
				stringz_lines[-1] += '\n' + line
	return stringz_offsets, stringz_lines

def get_translation(filepath: str) -> tuple[dict[str, str], dict[str, str]]:
	with open(filepath, 'r', encoding='utf-8') as f:
		translation: dict[str, str] = json.loads(f.read())

	settings = translation[""]
	del translation[""]

	return translation, settings

def slice_offsets(offsets: str, start = None, end = None) -> str:
	if start is None and end is None:
		return offsets
	offsets_beg, offsets = offsets.split('-', 1)
	offsets, offsets_end = offsets.rsplit('___', 1)
	offsets = '-'.join(offsets.split('-')[start:end])
	return f"{offsets_beg}-{offsets}___{offsets_end}"

def replace_with_table(string: str, table: dict[str, str]) -> str:
	for key, value in table.items():
		string = string.replace(key, value)
	return string