def secure_name(name):
    """
    name에서 성을 제외한 이름을 *로 변환해주는 함수!
    :param name: 3글자의 성 + 이름
    :return: 성 + **
    """
    return name[0] + '**'


def secure_no(no):
    """
    주민번호에서 뒷자리 첫번째를 제외한 나머지를 *로 변환해주는 함수
    :param no: 주민번호
    :return: 주민번호 앞자리 + 뒷자리 1번째 + ******
    """
    #950701 -1234567
    return no[0:8] + '******'

def secure_phone(phone):
    """
    전화번호에서 중간자리 번호를 *로 변경해준다!

    :param phone: 전화번호
    :return: 010-****-5767
    """
    return phone.replace(phone[4:8],'****')