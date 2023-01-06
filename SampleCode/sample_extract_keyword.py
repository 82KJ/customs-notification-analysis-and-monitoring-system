'''
FileName : scraper/extract_keyword.py
Summary : 문서에서 키워드를 추출하는 모듈
'''

# ======================================================================
# Sample code of extracting keyword
# ======================================================================

'''
Description: 문서를 bigram 단위로 토큰화하기 위한 함수
Parameter: doc_list(전체 문서들의 list (type: list))
Return: candidate_list(문서에서 추출된 bigram들의 list (type: list))
'''
def bigram(doc_list):
    n_gram_range = (2, 2)
    candidate_list = []
    for doc in doc_list:
        count = CountVectorizer(ngram_range=n_gram_range, stop_words='english').fit([doc])
        candidate = count.get_feature_names_out()
        candidate_list.append(candidate)

    return candidate_list

# ======================================================================================================================================================================#
# All the code below has been removed as a private area.

# '''
# Description: 문서 리스트와 문서의 bigram들을 embedding 한 후, 코사인 비교를 통해 문서를 대표할 수 있는 bigram list를 뽑아내기 위한 함수
# Parameter: removed
# Return: removed
# '''
# def bigram_embedding(): pass
   
# '''
# Description: 문서를 대표할 수 있는 바이그램(문서와의 코사인 유사도가 높은 상위 20개의 문서 내 바이그램)의 임베딩 값을 추출하기 위한 함수
# Parameter: removed
# Return: removed
# '''
# def keyword_embedding(): pass    

# '''
# Description: 문서에서 추출한 바이그램과 주요 수출입 품목의 코사인 유사도를 비교해서 자체적으로 설정한 기준값을 넘는 경우의 바이그램, 주요 수출입 품목, 코사인 유사도 거리를 추출하는 함수
# Parameter: removed
# Return: removed
# '''
# def similarity_test(): pass

# '''
# Description: 해당 국가의 MTI 4단위 키워드를 가져오기 위한 함수
# Parameter: removed
# return: removed
# '''
# def get_keyword4(): pass

# '''
# Description: 해당 국가의 MTI 6단위 키워드를 가져오기 위한 함수
# Parameter: removed
# return: removed
# '''
# def get_keyword6(): pass

# '''
# Description: 매칭된 mti 4단위 단어들과 연관된 mti 6단위 세부 품목들을 뽑아내기 위한 함수
# Parameter: removed
# Return: removed
# '''
# def final_keyword6(): pass

# '''
# Description: 매칭된 6단위 mti 코드와 연관된 4단위 mti 코드를 추출하기 위한 함수
# Parameter: removed
# Return: removed
# '''
# def final_keyword4(): pass
# '''
# Description: 최종 매칭표를 출력하기 위한 함수로, 각 문서마다 생성되며 데이터 프레임이 비어 있는 경우 키워드가 추출되지 않았음을 의미
# Parameter: removed
# return: removed
# '''
# def make_df(): pass