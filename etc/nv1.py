'''
필터링해서 남은 이메일 찾기
'''


def solution(emails):
    answer = 0

    for email in emails:

        try:

            name = email.split("@")

            if len(name) > 2:
                continue

            # if "a" > name[0] or name[0] > "z":  # . 은 고려안했는데.... 어떡하지 ?
            #     continue  # next for
            # flag = 0
            # for _name in name[0]:
            #     if "a" <= _name <= "z" or _name == ".":
            #         continue
            #     else:
            #         flag = 1
            #         break
            # if flag:
            #     continue

            domain = name[1].split(".")

            if len(domain) > 2:
                continue

            # if "a" >= domain[0] or domain[0] >= "z":
            #     continue

            topLevelDomain = domain[1]

            # if topLevelDomain == "com" or topLevelDomain == "net" or topLevelDomain == "org":
            if topLevelDomain in ['com', 'net', 'org']:
                # print("###", name[0], domain[0], domain[1])
                answer += 1
        except IndexError as identifier:
            pass
    return answer


# emails = ["d@co@m.com", "a@abc.com", "b@def.com", "c@ghi.net"]
# emails = ["abc.def@x.com", "abc", "abc@defx", "abc@defx.xyz"]
# emails = ["dco@m.com", "dc.o@m.com", "A@abc.com"]
emails = ["a.aa@abc.com"]

print(solution(emails))
