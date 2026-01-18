pool_volume = int(input())
pipe_one_volume_flow = int(input())
pipe_two_volume_flow = int(input())
hours_employe_gone = float(input())

volume_pipe_one = pipe_one_volume_flow * hours_employe_gone
volume_pipe_two = pipe_two_volume_flow * hours_employe_gone
total_volume = volume_pipe_one + volume_pipe_two
if total_volume < pool_volume:
    volume_in_procents = (total_volume / pool_volume) * 100
    volume_in_procents_pipe_one = (volume_pipe_one / total_volume) * 100
    volume_in_procents_pipe_two = (volume_pipe_two / total_volume) * 100
    print(f"The pool is {volume_in_procents:.2f}% full. Pipe 1: {volume_in_procents_pipe_one:.2f}%. Pipe 2: {volume_in_procents_pipe_two:.2f}%.")

else:
    print(f"For {hours_employe_gone} hours the pool overflows with {total_volume - pool_volume:.2f} liters.")