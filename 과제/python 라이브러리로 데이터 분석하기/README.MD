## pandas를 이용하여 데이터 분석
print를 사용하여 출력할 경우 DataFrame 출력의 가독성이 낮아 DataFrame를 할당한 변수를 직접 출력. 

필수 과제
1. Python 라이브러리 함수를 사용하여 엑셀 파일을 불러오고, DataFrame을 출력해주세요.
pd.read_excel를 이용하여 작업 폴더에 있는 관서별 5대범죄 발생 및 검거 파일 로드 및 출력. 

2. 각 경찰서(관서명)를 해당 구 이름으로 매핑하여 '구별'이라는 새로운 column을 생성하고, DataFrame을 출력해주세요.
- 구별 컬럼 생성하기 위한 딕셔너리 데이터를 입력(임시파일이라는 의미로 tmp로 변수 할당.), 이 데이터를 DataFrame로 변환하며 컬럼명을 '구별'로 입력
- 딕셔너리를 DataFrame로 변환시 가로 방향 DataFrame이므로 tmp.t를 이용하여 세로 방향으로 DataFrame 형태 변환.
- reset_index를 이용하여 초기에 설정된 index를 컬럼으로 이동 후 해당 컬럼명을 index에서 "관서명"으로 변환
- 관서명 컬럼을 기준으로 1번 문제의 DataFrame와 tmp DataFrame를 merge 함수를 이용하여 결합.
- fillna를 이용하여 빈 값을 '구없음'으로 대체

3. pivot_table 을 사용하여 관서별 데이터를 구별 데이터로 변경하고, 같은 구의 경우에는 sum을 적용하여 더해주세요. (index : 관서명 -> 구별)
- pivot_table 함수를 이용하여 피봇 테이블로 변환. index는 '구별' 컬럼을 사용.  aggfunc = "sum"를 이용하여 같은 구의 경우에 sum을 적용. 
- drop를 이용하여 관서명 컬럼을 제거

4. 구 없음  행은 drop 을 활용하여 삭제해주세요.
- 문제마다 DataFrame를 구분
- drop를 이용하여 index가 '구없음'인 행을 제거. 

5. 각 범죄 별로 검거율을 계산하고, 각 검거율 데이터 column을 DataFrame에 추가해주세요.
- 문제마다 DataFrame를 구분
- 범죄 종류 리스트를 생성
- 검거율 컬럼 생성 및 (검거/발생)*100의 값을 할당. 
- 범죄 종류 리스트를 이용한 반복문으로 범죄별 검거율 컬럼 생성 및 검거율 계산 값 할당. 

6. 필요없는 column을 del 을 사용하여 삭제해주세요.
- 문제마다 DataFrame를 구분
- 삭제해야 할 컬럼 리스트를 생성. 
- 반복문과 del을 이용하여 삭제해야 할 컬럼들을 삭제. 

7. DataFrame의 컬럼명을 rename 을 사용하여 변경해주세요.
- 문제마다 DataFrame를 구분
- rename 함수와 기존값: 변경값 딕셔너리를 이용하여 컬럼명을 한번에 변환

추가과제
1. Python 라이브러리 함수를 사용하여 인구 데이터(pop_kor.csv) 파일을 불러오고, DataFrame을 출력해주세요.
pd.read_csv를 이용하여 작업 폴더에 있는 관서별 5대범죄 발생 및 검거 파일 로드 및 출력. index_col을 이용하여 '구별'을 인덱스로 설정

2. join 을 사용하여 Quiz에서 수행한 DataFrame과 인구 데이터 DataFrame을 merge하고, DataFrame을 출력해주세요.
join은 index를 기준으로 merge를 수행하는 함수.

3. 새롭게 merge 된 DataFrame에서 검거율 기준으로 오름차순 정렬 후, DataFrame을 출력해주세요.
sort_values('검거율',ascending= True)을 이용하여 검거율 기준으로 오름차순 정렬
