# [2020 KAKAO BLIND RECRUITMENT] 문자열 압축
def solution(s):
    min_s_len = len(s)
    for i in range(1, len(s)//2 + 1):
        sliced_s = [s[idx:idx+i] for idx in range(0, len(s), i)]
        # if sliced_s[0] != sliced_s[1]:
        #     continue

        compressed_s_list = []
        stack = []
        for a in sliced_s:
            if stack and stack[-1] != a:
                rep_count = len(stack)
                if rep_count == 1:
                    compressed_s_list.append(stack.pop())
                else:
                    compressed_s_list.append(str(rep_count) + stack.pop())
                    stack.clear()
            stack.append(a)
        if stack:
            rep_count = len(stack)
            if rep_count == 1:
                compressed_s_list.append(stack.pop())
            else:
                compressed_s_list.append(str(rep_count) + stack.pop())
        min_s_len = min(min_s_len, len(''.join(compressed_s_list)))
    return min_s_len

# 다른 사람의 풀이
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])
    
if __name__ == "__main__":
    print(solution("abcabcabcadqabcabc"))
    # print(solution("aabbaccc"))
    # print(solution("aabbaccc") == 7)
    # print(solution("ababcdcdababcdcd"))
    # print(solution("ababcdcdababcdcd") == 9)
    # print(solution("abcabcdede"))
    # print(solution("abcabcdede") == 8)
    # print(solution("abcabcabcabcdededededede"))
    # print(solution("abcabcabcabcdededededede") == 14)
    print(solution("xababcdcdababcdcd"))
    # print(solution("xababcdcdababcdcd") == 17)