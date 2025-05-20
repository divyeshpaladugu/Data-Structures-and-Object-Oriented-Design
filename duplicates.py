def has_duplicates2(L): 

  """Checks every item in L against every *previous* item for duplicates""" 

  n = len(L)         # 2

  for i in range(n):     # n times

    for j in range(i):   # (i+1) times 

      if L[i] == L[j]:  # 3

        return True   # 1

  return False        # 1

                # ---------------- 

                # 2 + Sum_{i=0}{i=n-1}{3+0}+1

def has_duplicates3(L): 

  """Sorts list, then does a linear scan to find duplicates""" 

  n = len(L)       # 3

  L.sort()        # 0(nlogn)

  for i in range(n-1):  # n-1 times

    if L[i] == L[i+1]: # 4 (L[i], i+1, L[i+1], ==)

      return True   # 

  return False      # 1

              # -------------- 

           # 2 + 0(nlogn) + (n-1) * (4+0) + 1
            # 0(nlogn) + 4n - 1

 

# Major improvement 2 - just do a bunch of linear operations 

def has_duplicates4(L): 

  """Creates a set of L, checks it's length against L""" 

  s = set(L)       # 0(n)

  return len(s) == len(L) # 3 (len(s), len(L), ==)

              # -------- 