import random

dna = ["TTACCTTAAC", "GATGTCTGTC", "ACGGCGTTAG", "CCCTAACGAG", "CGTCAGAGGT"]

dna2 = ["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA", "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG", "TAGTACCGAGACCGAAAGAAGTATACAGGCGT", "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC", "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]

#k = 8


def CountWithPseudocounts(Motifs):
  count = {}
  k = len(Motifs[0])  #6
  for symbol in "ACGT":
    count[symbol] = []
    for j in range(k):
      count[symbol].append(1)
  t = len(Motifs) #5
  for i in range(t):
    for j in range(k):
      symbol = Motifs[i][j]
      count[symbol][j] += 1
  return count
  
def ProfileWithPseudocounts(Motifs):
  t = len(Motifs) #5
  k = len(Motifs[0]) #6
  profile = {}
  motifmatrix = CountWithPseudocounts(Motifs)
  for key in motifmatrix:
    symbolPercentages = []
    for symbolCount in motifmatrix[key]:
      symbolPercentages.append(symbolCount/(t+4))
    profile[key] = symbolPercentages
  return profile
  
def Consensus(Motifs):
  k = len(Motifs[0])
  count = CountWithPseudocounts(Motifs)
  consensus = ""
  for j in range(k):
    m = 0
    frequentSymbol = ""
    for symbol in "ACGT":
      if count[symbol][j] > m:
        m = count[symbol][j]
        frequentSymbol = symbol
    consensus += frequentSymbol
  return consensus  
  
def Score(Motifs):
  k = len(Motifs[0])
  t = len(Motifs)
  count = CountWithPseudocounts(Motifs)
  consensus = Consensus(Motifs)
  score = 0
  for i in range(k):
    currentSymbol = consensus[i]
    symbolCount = count[currentSymbol][i]
    score += t - symbolCount
  return score
  
def Pr(Text, Profile):
  p = 1
  k = len(Text)
  for i in range(k):
    p *= Profile[Text[i]][i]
  return p
  
def ProfileMostProbablePattern(Text, k, Profile):
  highestProb = -1
  pattern = ""
  for i in range(len(Text)-k+1):
    if Pr(Text[i:i+k], Profile) > highestProb:
      highestProb = Pr(Text[i:i+k], Profile)
      pattern = Text[i:i+k]
  return pattern
  
  
def Motifs(Profile, Dna):
  probableKmers = []
  for string in Dna:
    mostCommonKMer = ProfileMostProbablePattern(string, len(Profile["A"]), Profile)
    probableKmers.append(mostCommonKMer)
  return probableKmers


def RandomMotifs(Dna, k):
  randomStrings = []
  for string in Dna:
    m = len(string)
    r = random.randint(0, m-k)
    randomChoice = string[r:r+k]
    randomStrings.append(randomChoice)
  return randomStrings

def RandomizedMotifSearch(Dna, k):
  M = RandomMotifs(Dna, k)
  BestMotifs = M
  while True:
    Profile = ProfileWithPseudocounts(M)
    M = Motifs(Profile, Dna)
    if Score(M) < Score(BestMotifs):
      BestMotifs = M
    else:
      return BestMotifs
  
  
  
  
print ("The randomized motifs are")  
print (RandomizedMotifSearch(dna2, 8))
print ("\n")
    


print ("M is")  
print (RandomMotifs(dna2, 8))
print ("\n")
print ("Profile matrix of M is")
print (ProfileWithPseudocounts(RandomMotifs(dna2, 8)))
print ("\n")
print ("The probable motifs are")
print (Motifs(ProfileWithPseudocounts(RandomMotifs(dna2, 8)), dna2))
print ("\n")


#repeat function N number of times

N = 10
  
results = {}

for i in range(N):
  kmerLength = 8
  randomMotif = RandomizedMotifSearch(dna2, kmerLength)
  scoreOfMotif = Score(randomMotif)
  results[scoreOfMotif] = randomMotif

highestMotifScore = sorted(results.keys())[-1]
BestMotifs = results[highestMotifScore]

print (BestMotifs)
print (highestMotifScore)
print ("\n")
print ("**Currently using hard-coded DNA string. Could be altered to take user input instead.")


  
  

    
    
    
    
    
    
    
    
    
    
    
    
  