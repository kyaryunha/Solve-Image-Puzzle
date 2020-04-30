## Solve Image Puzzle by Human Intelligence

이 레포지토리는 https://codeforces.com/blog/entry/70047 에 참가하는 신 현(kyaryunha)와 심유근(16silver), 박수현(shiftpsh)의 private repository(추후 Public으로 전환)로, 작업 기간은 2~3일 정도입니다.


### Goal
k x k의 이미지 퍼즐이 있을 때, ( k = 8, 16, 32 ) 그 퍼즐을 재배치하는 수열을 생성합니다.

AI를 모르므로, 사람의 지능으로 푸는 방식을 택했습니다. 

### Development
- Python, OpenCV

### How to?
- 먼저 kyaryunha64.py, kyaryunha32.py, kyaryunha 16.py (각각 8, 16, 32에 대응)는 랜덤의 점수를 받기 위해, 랜덤의 수열을 생성하여 파일입출력으로 test1_64.txt, test1_32.txt, test1_16.txt에 저장합니다.
- kyaryunha64_MouseGame.py ( 8 x 8 퍼즐에 대응 )는 정확한 점수를 받기 위해, 퍼즐을 직접 풀 수 있도록 하였습니다. `사람`이 직접 퍼즐을 풀고, 그 결과 값을 수열에 반영하여, 퍼즐이 풀려졌을 때, 그 퍼즐을 재배치하는 수열을 저장합니다. 
- kyaryunha64_TextToImg.py는 텍스트 파일이 있을 때, 해당 텍스트에 대응하는 이미지를 만들어 줍니다. 수열이 있을 때, 이 수열로 퍼즐을 만들었을 때, 제대로 만들어지는지를 디버깅하기 위하여 만들었습니다. 
- kyaryunha64_solving.py는 셔플 이미지와 완성 이미지가 있을 때 수열을 찾아줍니다. TextToImg랑 반대로, ShuffleToImg인 셈입니다. 프로젝트가 현재 인간지능을 기반으로 하고 있고, 추후 휴리스틱의 방식을 하게 될 때, Cost를 계산하기 위한 목적으로 만들려고 하였습니다. 픽셀 비교의 방식으로 제작하려 하였으나, 이미지 처리 능력이 좋지 않아서 현재 거의 안돌아갑니다. 

### List
현재 파일 목록은 다음과 같습니다.

- kyaryunha64.py : A번 문제에 대해서 랜덤 수열 생성해서, test1_64에 저장
- kyaryunha32.py : B번 문제에 대해서 랜덤 수열 생성해서, test1_32에 저장
- kyaryunha16.py : C번 문제에 대해서 랜덤 수열 생성해서, test1_16에 저장
- kyaryunha64_MouseGame.py : 마우스 게임을 통해 퍼즐을 풀 수 있다!
- kyaryunha64_TextToImg.py : 텍스트 파일이 있을 때, 해당 텍스트에 대응하는 이미지를 만들어준다.
- kyaryunha64_solving.py : 셔플 이미지와, 완성 이미지가 있을 떄 수열을 찾아준다.(는 거의 안돌아감. o_o)
