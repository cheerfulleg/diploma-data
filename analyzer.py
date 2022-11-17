import glob
import logging
import os
import shutil

import radon.raw
from git.repo.base import Repo

logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)


class Analyzer:
    RESTRICTIONS = ['venv', '__pycache__', '.idea']
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    @staticmethod
    def _analyze(source: str) -> dict:
        analytics = radon.raw.analyze(source)._asdict()
        analytics['classes_qnt'] = source.count('class ')
        analytics['functions_qnt'] = source.count('def ')
        logger.info(analytics)
        return analytics

    def _get_source_code(self, repo: str) -> str:
        source = ''
        for filename in glob.iglob(f'{repo}**/**', recursive=True):
            if all(x not in filename for x in self.RESTRICTIONS) and filename.endswith('.py'):
                with open(filename, 'r') as f:
                    source += f.read() + '\n'
        return source

    @staticmethod
    def _download_project(repo: str):
        url = f'https://github.com/{repo}'
        Repo.clone_from(url, repo)

    def _delete_directory(self, repo: str):
        delete_dir = os.path.join(self.BASE_DIR, repo.split('/')[0])
        shutil.rmtree(delete_dir)
        logger.info(f'{repo} deleted')

    def get_metrics(self, repos: list[str]) -> list[dict]:
        result = []
        for repo in repos:
            try:
                self._download_project(repo)
            except Exception as e:
                logger.error(e)
                break

            try:
                source = self._get_source_code(repo)
                result.append(self._analyze(source))
            except Exception as e:
                logger.error(e)
            finally:
                self._delete_directory(repo)
        return result
