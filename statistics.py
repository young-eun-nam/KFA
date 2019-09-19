import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# 그래프에서 마이너스 폰트 깨지는 문제에 대한 대처
mpl.rcParams['axes.unicode_minus'] = False

pd.set_option("display.max_columns", 30)
pd.set_option("display.max_rows", 100)

U13_CSV_FILE = "측정결과_U13.csv"
U14_CSV_FILE = "측정결과_U14.csv"
U15_CSV_FILE = "측정결과_U15.csv"
PYTHON = 'python'

# 테스트 지표 Column 명
REACTIVE_AGILITY = 'Reactive Agility'
TEN_METER_SPRINT = '10m Sprint'
THIRY_METER_SPRINT = '30m Sprint'
GERMANY_WITHOUT_BALL = 'Germany Test without Ball'
GERMANY_WITH_BALL = 'Germany Test with Ball'
BALL_CONTROL = 'Ball Control'
TEST_INDEX_ARRAY = [[REACTIVE_AGILITY, TEN_METER_SPRINT], [THIRY_METER_SPRINT, GERMANY_WITHOUT_BALL], [GERMANY_WITH_BALL, BALL_CONTROL]]

# 그룹
GOLDEN_AGE = 'S. 영재센터'
PRO_YOUTH = 'A. 프로산하'
WEEKEND_LEAGUE = 'B. 주말리그'

# 라벨
GOlDEN_AGE_LABEL = 'Golden Age'
PRO_YOUTH_LABEL = 'Pro Youth'
WEEKEND_LEAGUE_LABEL = 'Weekend League'


def drop_na(dataframe):
    refined_df = dataframe.dropna()
    return refined_df

def select_columns(selected_column, row, col):
    cal_df_golden = test_results[test_results['구분'] == GOLDEN_AGE][selected_column]
    cal_df_pro = test_results[test_results['구분'] == PRO_YOUTH][selected_column]
    cal_df_weekend = test_results[test_results['구분'] == WEEKEND_LEAGUE][selected_column]
    cal_df_golden = drop_na(cal_df_golden)
    cal_df_pro = drop_na(cal_df_pro)
    cal_df_weekend = drop_na(cal_df_weekend)
    draw_distplot(selected_column, cal_df_golden, cal_df_pro, cal_df_weekend, row, col)

def draw_distplot(selected_column, cal_df_golden, cal_df_pro, cal_df_weekend, row, col):
    graph_distplot = sns.distplot(cal_df_golden, bins=30, color='#80ccb7', ax=axes[row, col], label=GOlDEN_AGE_LABEL)
    sns.distplot(cal_df_pro, bins=30, color='r', ax=axes[row, col], label=PRO_YOUTH_LABEL)
    sns.distplot(cal_df_weekend, bins=30, color='b', ax=axes[row, col], label=WEEKEND_LEAGUE_LABEL)
    graph_distplot.set_title(selected_column)
    if row == 2:
        graph_distplot.set_xlabel('time(seconds)')
    else:
        graph_distplot.set_xlabel('')
    graph_distplot.set_ylabel('players')
    graph_distplot.legend()

if __name__ == "__main__":
    test_results = pd.read_csv(U15_CSV_FILE, engine=PYTHON)
    sns.set()
    f, axes = plt.subplots(3, 2, figsize=(15, 15))
    for row in range(len(TEST_INDEX_ARRAY)):
        for col in range(len(TEST_INDEX_ARRAY[row])):
            select_columns(TEST_INDEX_ARRAY[row][col], row, col)
    plt.show()