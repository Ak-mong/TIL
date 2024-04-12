from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import numpy as np
# Create your views here.


def index(request):
    return render(request, 'weathers/index.html')

def problem1(request):
    '''
    다운로드 받은 데이터(.csv) 를 Pandas DataFrame 형식으로 저장 및
    problem1.html 렌더링
    dataframe으로 읽어오기
    전체 데이터 표 형태로 출력
    ''' 
    # 파일을 읽어야 함
    csv_path = 'austin_weather.csv'
    df = pd.read_csv(csv_path)
    context = {
        'df':df
    }
    return render(request, 'weathers/problem1.html', context)

def problem2(request):
    # 파일을 읽어야 함
    csv_path = 'austin_weather.csv'
    df = pd.read_csv(csv_path, encoding='cp949')
    df['Date'] = pd.to_datetime(df['Date']) 

    # 그래프 초기화
    plt.clf()

    # 그리드 화
    plt.grid()

    # plot 생성
    plt.plot(df['Date'],df['TempHighF'], label='TempHighF')
    plt.plot(df['Date'],df['TempAvgF'], label='TempAvgF')
    plt.plot(df['Date'],df['TempLowF'], label='TempLowF')

    plt.title('Tempperature Variation')
    plt.xlabel('Date' )
    plt.ylabel('Temperature (Fahrenheit)')
    plt.legend()

    # 비어있는 버퍼 생성
    buffer = BytesIO()

    # buffer 에 그래프를 png 형태로 저장
    plt.savefig(buffer, format='png')

    # 버퍼의 내용을 인코딩
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n','')
    buffer.close()
    # print(img_base64)
    context = {
        'df':df,
        'image': f'data:image/png;base64,{img_base64}',
    }
    '''
    일 별 온도 비교를 위한 라인 그래프 생성 및 problem2.html 렌더링'''
    return render(request, 'weathers/problem2.html', context)

def problem3(request):
    # 그래프 초기화
    plt.clf()
    # 파일을 읽어야 함
    csv_path = 'austin_weather.csv'
    df = pd.read_csv(csv_path, parse_dates=['Date']) 
    '''
    월 별 온도 비교를 위한 라인 그래프 생성 및 problem3.html 렌더링'''
    df['Date'] = pd.to_datetime(df['Date'])
    months = df.groupby(df['Date'].dt.to_period('M')).mean(numeric_only=True).reset_index()
    # print(months)
    months['Date'] = pd.to_datetime(months['Date'].astype(str))
    # print(months.dtypes)

    # 그리드 화
    plt.grid()
    
    # plot 생성
    plt.plot(months['Date'],months['TempHighF'],label='TempHighF')
    plt.plot(months['Date'],months['TempAvgF'],label='TempAvgF')
    plt.plot(months['Date'],months['TempLowF'],label='TempLowF')

    plt.title('Tempperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature (Fahrenheit)')
    plt.legend()

    # 비어있는 버퍼 생성
    buffer = BytesIO()

    # buffer 에 그래프를 png 형태로 저장
    plt.savefig(buffer, format='png')

    # 버퍼의 내용을 인코딩
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n','')
    buffer.close()
    # print(img_base64)
    context = {
        'df':df,
        'image': f'data:image/png;base64,{img_base64}',
    }
    return render(request, 'weathers/problem3.html', context)

def problem4(request):
    '''
    기상 현상 발생 횟수 히스토그램 생성 및 problem4.html 렌더링
    '''
    # 파일을 읽어야 함
    csv_path = 'austin_weather.csv'
    df = pd.read_csv(csv_path) # 
    # 그래프 초기화
    plt.clf()

    # df['Events'].fillna('No events', inplace=True)
    df['Events'].replace(' ','No Events', inplace=True)

    df_exploded = df['Events'].str.split(',').explode().str.strip()
 
    counts = df_exploded.value_counts()
    
    plt.figure(figsize=(10, 6))
    plt.bar(counts.index, counts.values)

    # 그리드 화
    plt.grid()

    plt.title('Event Counts')
    plt.xlabel('Events')
    plt.ylabel('Count')
    
    # 비어있는 버퍼 생성
    buffer = BytesIO()

    # buffer 에 그래프를 png 형태로 저장
    plt.savefig(buffer, format='png')

    # 버퍼의 내용을 인코딩
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n','')
    buffer.close()
    # print(img_base64)
    context = {
        'df':df,
        'image': f'data:image/png;base64,{img_base64}',
    }

    return render(request, 'weathers/problem4.html', context)