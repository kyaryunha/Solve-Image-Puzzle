## Solve Image Puzzle by Human Intelligence

이 레포지토리는 https://codeforces.com/blog/entry/70047 에 참가하는 신 현(kyaryunha)와 심유근(16silver), 박수현(shiftpsh)의 private repository(추후 Public으로 전환)로, 작업 기간은 2~3일 정도다.



### Development Skill

- Python, OpenCV




### Goal
k x k의 이미지 퍼즐이 있을 때, ( k = 8, 16, 32 ), 해당 퍼즐을 재배치하는 수열을 생성한다.

AI를 모르므로, 사람의 지능으로 푸는 방식을 택한다.



아래 이미지 중, 위의 이미지를 아래 이미지처럼 "사람이" 마우스 클릭을 통해 퍼즐을 푼다. 

퍼즐을 푸는 것이 종료되면, 마우스 클릭을 역추적하여, 재배치하는 수열을 생성한다.



###### Problem Image Example 

<img src="/example/example.png" width="300" height="300" align="left">



###### Answer Image Example

<img src="/example/example-ans.png" width="300" height="300" align="left">



최종적인 답은 다음과 같은 모양이다. (위 문제의 답은 아님.)

```
28 33 39 1 21 29 41 36 43 51 0 47 13 42 31 35 54 46 45 2 62 49 38 26 44 24 9 17 30 7 18 25 55 52 15 5 23 48 16 34 4 50 57 14 8 37 53 10 12 19 3 63 61 56 32 6 20 58 11 59 40 27 60 22 
```





### How to?
- random64.py, random32.py, random16.py (각각 8, 16, 32에 대응)

  - 랜덤의 점수를 받기 위해, 랜덤의 수열을 생성하여 파일입출력으로 test1_64.txt, test1_32.txt, test1_16.txt에 저장합

- 64_MouseGame.py ( 8 x 8 퍼즐에 대응 )

  - 정확한 점수를 받기 위해, 퍼즐을 직접 풀 수 있도록 함. `사람`이 직접 퍼즐을 푼다.
  - 그 결과 값을 수열에 반영하여, 퍼즐이 풀려졌을 때, 그 퍼즐을 재배치하는 수열을 저장

- 64_TextToImg.py

  - 텍스트 파일이 있을 때, 해당 텍스트에 대응하는 이미지를 만들어줌.
  - 수열이 있을 때, 이 수열로 퍼즐을 만들었을 때, 제대로 만들어지는지를 디버깅하기 위한 목적 

- 64_solving.py (**TODO**)

  - 셔플 이미지와 완성 이미지가 있을 때 수열 찾기
- TextToImg랑 반대로, ShuffleToImg인 셈
  - 프로젝트가 현재 인간지능을 기반으로 하고 있고, 추후 휴리스틱의 방식을 하게 될 때, Cost를 계산하기 위한 목적으로 만들려고 함. 픽셀 비교의 방식으로 제작하려 하였으나, 이미지 처리 능력이 좋지 않아서 현재 거의 안돌아감
  
  

### List
현재 파일 목록은 다음과 같다

- random64.py : A번 문제에 대해서 랜덤 수열 생성해서, test1_64에 저장
- random32.py : B번 문제에 대해서 랜덤 수열 생성해서, test1_32에 저장
- random16.py : C번 문제에 대해서 랜덤 수열 생성해서, test1_16에 저장
- 64_MouseGame.py : 마우스 게임을 통해 퍼즐을 풀 수 있다!
- 64_TextToImg.py : 텍스트 파일이 있을 때, 해당 텍스트에 대응하는 이미지를 만들어준다.
- 64_solving.py : 셔플 이미지와, 완성 이미지가 있을 떄 수열을 찾아준다.(는 거의 안돌아감. o_o)
