# toto123

### 파이썬 배포 가능한 패키지 만들기

### History
2022/02/22 레포지트리 만들기

### 절차
 - 01. 깃허브 레포지토리 만들기.
   - 만들기 전에 동일한 이름이 존재할 수 있으니, https://pypi.org/project/ 에 검색후, 진행한다. 동일한 것이 있을때, 에러 발생.
 - 02. 아나콘다 환경 세팅
   - conda create -n ccpy python=3.6
 - 03. Setup.py를 만들기
 - 04.  setup.py 실행
   ```
   (toto123) C:\Users\totofriend\Documents\GitHub\toto123>python setup.py bdist_wheel
   ```
    - 결과적으로 dist 폴더 생성. 폴더 안에 toto123-0.1-py3-none-any.whl가 생성.
 - 05. 배포
   - pip install twine or conda install twine
   - (toto123) C:\Users\totofriend\Documents\GitHub\toto123>twine upload dist/toto123-0.1-py3-none-any.whl
   ```
   (toto123) C:\Users\totofriend\Documents\GitHub\toto123>twine upload dist/toto123-0.1-py3-none-any.whl
   Uploading distributions to https://upload.pypi.org/legacy/
   Enter your username:
   ```
    - 아이디와 비밀번호 만들기
      - https://upload.pypi.org/legacy/
    - 만든 후 시도
    ```
    Enter your username: totofriend
    Enter your password:
    Uploading toto123-0.1-py3-none-any.whl
    100%|█████████████████████████████████████████████████████████████████████████████| 4.66k/4.66k [00:01<00:00, 3.83kB/s]
    Error during upload. Retry with the --verbose option for more details.
    HTTPError: 400 Bad Request from https://upload.pypi.org/legacy/
    User 'totofriend' does not have a verified primary email address. Please add a verified primary email before attempting to upload to PyPI. See https://pypi.org/help/#verified-email for more information.

    ```
    - 에러 발생 - 메일 확인 후, 링크 클릭 후, 진행
    ```
    Someone, perhaps you, has added this email address (frontier1020@naver.com) to their PyPI account.
    If you wish to proceed with this request, click this link to verify your email address.
    This link will expire in 72 hours.
    If you did not make this request, you can safely ignore this email.
    ```
    - 만약 같은 패키지가 존재하지 않으면 잘 진행됨.
    ```
    (toto123) C:\Users\totofriend\Documents\GitHub\toto123>twine upload dist/toto123-0.1-py3-none-any.whl
    Uploading distributions to https://upload.pypi.org/legacy/
    Enter your username: totofriend
    Enter your password:
    Uploading toto123-0.1-py3-none-any.whl
    100%|█████████████████████████████████████████████████████████████████████████████| 4.66k/4.66k [00:02<00:00, 1.88kB/s]

    View at:
    https://pypi.org/project/toto123/0.1/
    ```
    - * 만약 패키지가 존재하면 에러가 발생되니, 이를 위해서는 https://pypi.org/project/ 에 검색 후, 프로젝트를 진행하는 것이 좋을 듯.

 - 06. 실제 설치 - colab 환경에서
    - pip install toto123
    ```
    Collecting toto123
    Downloading toto123-0.1-py3-none-any.whl (1.1 kB)
    Installing collected packages: toto123
    Successfully installed toto123-0.1
    ```
    
### setpy.py

```
from setuptools import setup, find_packages

setup(
    name                = 'toto123',
    version             = '0.1',
    description         = 'toto123',
    author              = 'ldjwj',
    author_email        = 'colabstart@gmail.com',
    url                 = 'https://github.com/LDJWJ/toto123/',
    download_url        = 'https://github.com/LDJWJ/toto123/archive/0.0.tar.gz',
    install_requires    =  [],
    packages            = find_packages(exclude = []),
    keywords            = ['toto123'],
    python_requires     = '>=3',
    package_data        = {},
    zip_safe            = False,
    classifiers         = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
```
