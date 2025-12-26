import ctypes
import os

def trigger_bsod():
    # 1. 관리자 권한 확인 (BSOD 유발을 위해 필요)
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("관리자 권한이 필요합니다.")
        return

    # 2. ntdll.dll 로드
    ntdll = ctypes.windll.ntdll

    # 3. 프로세스를 'Critical' 상태로 설정
    # 이 설정이 활성화된 상태에서 프로세스가 죽으면 윈도우는 블루스크린을 띄웁니다.
    # RTL_SET_PROCESS_IS_CRITICAL(NewValue, OldValue, CheckPrivilege)
    ntdll.RtlSetProcessIsCritical(1, 0, 0)

    print("[!] 5초 후 시스템이 중단됩니다. 모든 작업 내용이 손실될 수 있습니다.")
    import time
    time.sleep(5)

    # 4. 프로세스 강제 종료 -> 즉시 블루스크린 발생
    os._exit(0)

if __name__ == "__main__":
    # 실제 실행 시 주의하세요! 
    # 가상 머신(VM) 환경 권장
    trigger_bsod()