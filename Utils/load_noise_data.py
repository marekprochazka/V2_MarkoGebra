from Utils.generate_noise import generate_noise

def load_noise_data(data:list):
    result = [[],[]]
    for value in data[0]:
        noise, _ = generate_noise(seed=value[1],dispersion=value[2],quantity=value[3])
        result[0].append(value + (noise,))
    return result