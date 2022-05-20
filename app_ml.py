import streamlit as st
import joblib
def run_ml() :
    st.subheader('자동차 구매 가능 금액 예측')

    # 예측하기 위해선, 필요한 파일들을 불러와야 된다.
    # 이 예시에서는, 인공지능파일, X스케일러 파일, y스케일러파일
    # 3개를 불러와야 한다.

    regressor = joblib.load('data/regressor.pkl')
    scaler_X = joblib.load('data/scaler_X.pkl')
    scaler_y = joblib.load('data/scaler_y.pkl')

    # 성별, 나이, 연봉, 카드빚, 자산을 입력받도록 만드세요

    gender = st.radio('성별 입력', ['남자','여자'])

    if gender == '여자' :
       gender = 0
    
    else :
        gender = 1

    age= st.number_input('나이 입력',0,120)
    salary= st.number_input('연봉 입력',0)
    debt= st.number_input('카드빚 입력',0)
    worth= st.number_input('자산 입력',0)


