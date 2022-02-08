from collections import defaultdict

word_f = open("words")
possible_f = open("possible_words")
words_og = [x.strip() for x in word_f.readlines()]
words = [x.strip() for x in possible_f.readlines()]

chars = defaultdict(lambda: 0)

# Compute most common characters.
for w in words:
    for ch in w:
        chars[ch] += 1

chars = dict(chars)
weights = dict(sorted(chars.items(), key=lambda x:x[1], reverse=True))

wrong = set()
# (char, position)
correct = {}
# (char, set() of wrong position)
exists = {}

unchecked = set("abcdefghijklmnopqrstuvwxyz")

elim_mode = False

def is_bad(w):
    # do not add words that conflict with known char positions
    for known, pos in correct.items():
        if w[pos] != known: return False
    
    # 2. do not add words containing known non-existent characters
    for ch in wrong:
        if ch in w: return False
    
    # 3. do not add words not containing known characters OR are
    #    in the wrong position
    for known, wrong_positions in exists.items():
        if not known in w: return False
        for wp in wrong_positions:
            if w[wp] == known: return False 
        
    return True

def filter_words():
    global words

    words = list(filter(lambda w: is_bad(w), words))
    print(f"\nRemaining words left: {len(words)}.\n")

def find_elim():
    max_val = 0
    max_word = ""
    
    unchecked_now = set()
    for w in words:
        for ch in w:
            if ch in unchecked: unchecked_now.add(ch)

    for w in words_og:
        # rank words based on their number of unchecked characters
        seen = set()
        val = 0
        for ch in w:
            if not ch in seen and ch in unchecked_now:
                val += 1
                seen.add(ch)
        
        if val > max_val:
            max_val = val
            max_word = w
    return max_word

def find_max():
    # 4. rank words by the remaining characters' weight
    max_val = 0
    max_word = ""

    if elim_mode:
        # return find_elim()
        potential = find_elim()
        if potential: return potential
    
    for w in words:
        # only consider characters' weight once to encourage distinct characters
        seen = set()
        v = 0
        for ch in w:
            if ch in seen: continue
            v += weights[ch]
            seen.add(ch)

        if v > max_val:
            max_val = v
            max_word = w

    return max_word

first = True
debug_first = False
will_win = False

i = 0
while i < 6:
    # print(f"i = {i}")
    if i == 5: elim_mode = False

    filter_words()

    elim_mode = not will_win \
            and (2 <= len(correct) <= 4) \
            and not len(words) == 1
    
    if elim_mode: print("NOTE: in elimination mode.")

    guess = find_max()

    if first: guess = "crane"
    first = False
    
    # if debug_first:
    #    print(correct, wrong, exists, words)
    
    print("Give your feedback on this word. Type 'skip' if this is not a valid word.")
    print(f"WORD:   \t\t{guess}")
    feedback = input("FEEDBACK:\t\t")

    if feedback == "skip":
        if guess in words:
            words.remove(guess)
        words_og.remove(guess)
        continue

    for i, ch in enumerate(feedback):
        cch = guess[i]
        if ch == "2" and not cch in correct:
            correct[cch] = i
            if cch in unchecked:
                unchecked.remove(cch)

        if ch == "1":
            if not cch in exists: exists[cch] = set()
            exists[cch].add(i)
            if cch in unchecked:
                unchecked.remove(cch)

        if ch == "0" and not cch in correct:
            wrong.add(cch)
            if cch in unchecked:
                unchecked.remove(cch)

    if not "0" in feedback:
        wil_win = True


    debug_first = True

    i += 1
