#!/usr/bin/env python3
sg=input('请输入一个身高：');
sg=float(sg);
tz=input('请输入一个体重：');
tz=float(tz);
BMI=(tz/2)/((sg/100)**2);
print('BMI值为：%.2f' % BMI);
if BMI<18.5:
    print('体重过轻');
elif BMI<24:
    print('体重正常');
elif BMI<27:
    print('体重过重');
else:
    print('体重肥胖');
