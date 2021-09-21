for i,name in enumerate(names):
  print(f'番号{i}の{name}')(='番号'+i+'の'+name)
# (インポートするだけでいいので標準ライブラリ)
import datetime
#今日の日付(date=日付、datetime=秒数まで知りたい時)
today = datetime.date.today()
datetime.datetime.now()
#今日の月
today.month(yearやdayも)
#昨日の日付
today - datetime.timedelta(days=1)
#フォーマット指定
today.strftime('%Y年%月%日')

