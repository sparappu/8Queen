import random

def f_Gene(size): #making random Genes 
    return [ random.randint(1, 8) for _ in range(8) ]

def f_fitness(Gene):
    h_col = sum([Gene.count(queen)-1 for queen in Gene])/2
    d_col = 0

    n = len(Gene)
    l_diag = [0] * 2*n
    r_diag = [0] * 2*n
    for i in range(n):
        l_diag[i + Gene[i] - 1] += 1
        r_diag[len(Gene) - i + Gene[i] - 2] += 1

    d_col = 0
    for i in range(2*n-1):
        counter = 0
        if l_diag[i] > 1:
            counter += l_diag[i]-1
        if r_diag[i] > 1:
            counter += r_diag[i]-1
        d_col += counter / (n-abs(i-n+1))
    
    return int(maxFitness - (h_col + d_col)) #28-(2+3)=23

def f_prob(Gene, fitness):
    return f_fitness(Gene) / maxFitness

def f_ran_pick(population, probabilities):
    populationWithProbabilty = zip(population, probabilities)
    total = sum(w for c, w in populationWithProbabilty)
    r = random.uniform(0, total)
    upto = 0
    for c, w in zip(population, probabilities):
        if upto + w >= r:
            return c
        upto += w
    assert False, "Shouldn't get here"
        
def f_crossover(x, y): #doing cross_over between two Genes
    n = len(x)
    c = random.randint(0, n - 1)
    return x[0:c] + y[c:n]

def f_mutate(x):  #randomly changing the value of a random index of a Gene
    n = len(x)
    c = random.randint(0, n - 1)
    m = random.randint(1, n)
    x[c] = m
    return x

def f_new_population(population, fitness):
    mutation_probability = 0.03
    new_population = []
    probabilities = [f_prob(n, fitness) for n in population]
    for i in range(len(population)):
        x = f_ran_pick(population, probabilities) #best Gene 1
        y = f_ran_pick(population, probabilities) #best Gene 2
        child = f_crossover(x, y) #creating two new Genes from the best 2 Genes
        if random.random() < mutation_probability:
            child = f_mutate(child)
        print_Gene(child)
        new_population.append(child)
        if f_fitness(child) == maxFitness: break
    return new_population

def print_Gene(gene):
    print("Gene = {},  Fitness = {}"
        .format(str(gene), f_fitness(gene)))

if __name__ == "__main__":
    maxFitness = 28  # 8*7/2 = 28
    population = [f_Gene(8) for _ in range(100)]
    fitness = 0
    
    generation = 1

    while not maxFitness in [f_fitness(gene) for gene in population]:
        print("=== Generation {} ===".format(generation))
        population = f_new_population(population, fitness)
        print("")
        print("Maximum Fitness = {}".format(max([f_fitness(n) for n in population])))
        generation += 1
    gene_out = []
    print("Solved in Generation {}!".format(generation-1))
    for gene in population:
        if f_fitness(gene) == maxFitness:
            print("");
            print("One of the solutions: ")
            gene_out = gene
            adj_l = [1]*8
            #print_Gene(gene)  
            #print(adj_l)
            difference = []
            zip_obj = zip(gene, adj_l)
            for gene, adj_l in zip_obj:
                difference.append(gene-adj_l)
            print(difference)