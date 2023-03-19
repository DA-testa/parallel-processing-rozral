#221RDB405 Ralfs Rozenbergs

def parallel_processing(n, m, data):
    output = []
    end_times = [0] * n
    for i in range(m):
        next_thread = end_times.index(min(end_times))
        start_time = end_times[next_thread]
        end_time = start_time + data[i]
        end_times[next_thread] = end_time
        output.append((next_thread, start_time))
    return output



def main():
    n, m = map(int,input().split())
    data = list(map(int,input().split()))
    for i in parallel_processing(n,m,data):
        print(i[0], i[1])



if __name__ == "__main__":
    main()