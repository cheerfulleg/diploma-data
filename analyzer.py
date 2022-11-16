import glob
import os
import shutil

import radon.raw
from git.repo.base import Repo


class Analyzer:
    RESTRICTIONS = ['venv', '__pycache__', '.idea']
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    @staticmethod
    def _analyze(source: str) -> dict:
        analytics = radon.raw.analyze(source)._asdict()
        analytics['classes_qnt'] = source.count('class ')
        analytics['functions_qnt'] = source.count('def ')
        return analytics

    def _get_source_code(self, repo: str) -> str:
        source = ''
        for filename in glob.iglob(f'{repo}**/**', recursive=True):
            if all(x not in filename for x in self.RESTRICTIONS) and filename.endswith('.py'):
                with open(filename, 'r') as f:
                    source += f.read() + '\n'
        return source

    def get_metrics(self, repos: list[str]) -> list[dict]:
        result = []
        for repo in repos:
            try:
                url = f'https://github.com/{repo}'
                Repo.clone_from(url, repo)
            except Exception as e:
                print(e)
                break
            try:
                source = self._get_source_code(repo)
                result.append(self._analyze(source))
            except Exception as e:
                print(e)
            finally:
                # delete downloaded project
                delete_dir = os.path.join(self.BASE_DIR, repo.split('/')[0])
                shutil.rmtree(delete_dir)
        return result
