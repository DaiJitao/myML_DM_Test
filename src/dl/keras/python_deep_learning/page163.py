state_t = 0
for input_t in input_sequence:
    output_t = f(input_t, state_t)
    state_t = output_t