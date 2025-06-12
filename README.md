## 참고 사진

![image](https://github.com/user-attachments/assets/787f7d1d-0900-4879-880b-f13f2d4ba653)

![캡처](https://github.com/user-attachments/assets/98d5f606-b819-4b76-835d-1e44e8d2da3c)


<br />

## 스마트팜 자동 제어 시스템 개요(Smart Farm Auto-Control System Overview)
본 장치는 라즈베리파이(Raspberry Pi)를 중심으로 구성된 자동 급수 및 환기 제어 시스템입니다.

습도 센서를 통해 토양 습도를 측정하고, 기준 이하일 경우 물통 + 수위 센서와 연동된 펌프를 통해 화단에 자동으로 물을 공급합니다.

팬은 설정 온도 이상일 때 자동 작동하여 내부 공기를 순환시킵니다.

센서 값은 라즈베리파이에서 실시간으로 수집되며, Python과 Flask 기반의 웹 대시보드를 통해 모니터링할 수 있습니다.  
(
This device is an automated irrigation and ventilation control system built around a Raspberry Pi.

A soil moisture sensor continuously monitors the soil condition. When the moisture level falls below a set threshold, the system automatically activates a water pump—linked to a water tank and water level sensor—to irrigate the garden.

A ventilation fan automatically turns on when the temperature exceeds a predefined limit, helping circulate air inside the system.

All sensor data is collected in real time by the Raspberry Pi and can be monitored via a web-based dashboard developed with Python and Flask.

)  

<br />

## 주요 구성(Key Components)

Raspberry Pi (제어 중심)

습도 센서 / 수위 센서

급수 펌프, 환기 팬

Flask 웹 서버 + SQLite 저장  
  
(
Raspberry Pi (main control unit)

Soil moisture sensor / Water level sensor

Water pump and ventilation fan

Flask web server with SQLite data storage

)
