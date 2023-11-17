from twilio.rest import Client
import streamlit as st
import time

def send_twilio_message(message_body, to_phone_number):
   
    account_sid = 'AC6ace276241c9dc6937210cc98a449a68'
    auth_token = 'a7d90f3377cfc6e62c1af55a784b0359'
    twilio_client = Client(account_sid, auth_token)

    try:
        message = twilio_client.messages.create(
            from_='+13344589434',
            body=message_body,
            to=to_phone_number
        )
        st.success("메시지가 성공적으로 전송되었습니다. SID: {}".format(message.sid))
    except Exception as e:
        st.error("메시지 전송 중 오류가 발생했습니다: {}".format(str(e)))

def show_message():
    st.title("안내메세지를 받아보세요!")

  
    message_body = '''
    
(안내)[KT안내]서울 지역 65세 이상 고객 대상 디지털 기기 무료 교육 및 요금 할인, 새로운 가족 결합 안내 

1) 서울 지역 65세 이상 고객에게만 드리는 디지털 기기 무료 교육 이벤트♥
가까운 디지털 배움터, 대리점, 플라자, 체험형 플라자에 방문하셔서 이용해 보세요!

▶무료 교육에 대해 자세히 알아보기 : 링크

서울 지역 디지털 기기 무료 교육
▶기간 : 2023.12.01.~2023.12.31.
▶대상 : 서울에 주소를 두고 있는 서울 특별 시민인 65세 이상 고객
▶장소 : 서울 전 지역의 디지털 배움터, 대리점, 플라자, 체험형 플라자
▶혜택 : 디지털 기기 무료 교육을 수료한 고객에게는 월 10% 요금 할인까지

2) 새로운 가족 결합 안내
인터넷 사용을 안 하신다고요? 5회선 이상 결합을 하고 싶으시다고요? 걱정마세요 저희 KT가 해드릴게요. 거기다 급하게 데이터가 필요한 고객님이라면 가족 간 데이터 공유도 가능합니다.

▶내용 : 인터넷 사용 안 하는 사람도 결합 가능, 회선 제한 X, 데이터 쉐어링 제한 없음

▶변경 전 : 5회선까지, 인터넷 + 모바일 결합 기준, 데이터 쉐어링 제한 있음

고객님을 위해 항상 최선을 다하는 KT가 되겠습니다.

감사합니다.

[마음을 담다 DIGICO KT]
        '''

    to_phone_number = st.text_input("수신자 전화번호", "+821046170614")

    send_twilio_message(message_body, to_phone_number)