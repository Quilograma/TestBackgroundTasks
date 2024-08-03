import numpy as np
from sklearn.utils import resample

# Defina a sua amostra
amostra = np.array([1, 2, 3, 0, -1, -2, -3, 1, 2, 3])

# Defina a média nula para o teste de hipóteses
media_nula = 0

# Defina o número de bootstrap samples
n_bootstrap = 1000

# Calcule as médias das amostras bootstrap
bootstrap_means = []
for _ in range(n_bootstrap):
    bootstrap_sample = resample(amostra)
    bootstrap_means.append(np.mean(bootstrap_sample))

bootstrap_means = np.array(bootstrap_means)

# Calcule o p-value
p_value = 2 * min(np.mean(bootstrap_means > media_nula), np.mean(bootstrap_means < -media_nula))

# Imprima o resultado
print("Média da amostra:", np.mean(amostra))
print("P-value:", p_value)

# Realize o teste de hipóteses
alpha = 0.05

if p_value < alpha:
    print("Rejeita a hipótese nula: A amostra não vem de uma população com média zero.")
else:
    print("Não há evidências para rejeitar a hipótese nula: A amostra pode vir de uma população com média zero.")
