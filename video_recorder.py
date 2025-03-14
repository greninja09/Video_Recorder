import cv2

# 영상 저장 설정
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 코덱 설정
fps = 24.0  # 초당 프레임 수
frame_size = (640, 480)  # 프레임 크기

# 웹캠 열기
cap = cv2.VideoCapture(0)
cap.set(3, frame_size[0])  # 너비 설정
cap.set(4, frame_size[1])  # 높이 설정

# 비디오 저장 설정
out = None
is_recording = False
flip_mode = False  # 좌우 반전 모드 여부

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # 좌우 반전 적용 여부 확인
    if flip_mode:
        frame = cv2.flip(frame, 1)
    
    # 녹화 중이라면 비디오 저장
    if is_recording:
        out.write(frame)
        cv2.circle(frame, (35, 40), 10, (0, 0, 255), -1)  # 빨간색 원 표시 (미리보기용)
        txt = "Recording" if not flip_mode else "Recording (Flip Mode)"
        cv2.putText(frame, txt, (35, 50), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0,0,0), thickness=2)   # 녹화 중 텍스트 표시
        cv2.putText(frame, txt, (35, 50), cv2.FONT_HERSHEY_DUPLEX, 0.6, (255,255,255))          # (미리보기용)


    cv2.imshow('Video Recorder', frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC 키로 종료
        break
    elif key == 32:  # Space 키로 녹화 시작/중지
        if is_recording:
            is_recording = False
            out.release()
        else:
            save_name = './data/output.avi' if not flip_mode else './data/output_fliped.avi'
            out = cv2.VideoWriter(save_name, fourcc, fps, frame_size)
            is_recording = True
    elif key == 9:  # Tab 키로 좌우 반전 토글
        flip_mode = not flip_mode

# 종료 처리
cap.release()
if out:
    out.release()
cv2.destroyAllWindows()
