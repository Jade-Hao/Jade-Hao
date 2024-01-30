def steps_analyzer(infile):
    count=0
    steps_total=0
    steps_max=0
    for line in infile.readlines():
        line=float(line.rstrip("\n"))
        count = count + 1
        if count < 8:
            steps_total+=line
            if line > steps_max:
                steps_max=line
        else:
            return (steps_total,steps_max)
    

def heart_rate_analyzer(infile):
    infile.seek(7)
    heart_rate_average=0
    heart_total=0
    accumulator=0
    count=7
    for line in infile.readlines():
        line=float(line.rstrip("\n"))
        accumulator=accumulator + 1 
        if accumulator>6 and accumulator<14:
            heart_total+=line
    heart_rate_average= heart_total/count
    return (heart_rate_average)


def sleep_analyzer(infile):
    infile.seek(0)
    total=0
    sleep_total=0
    sleep_min=100
    for line in infile.readlines():
        total=total+1
        if total > 14 and total <= 21:
            line = float(line.rstrip("\n"))
            sleep_total += line
            if line < sleep_min:
                sleep_min = line
    
    return (sleep_total, sleep_min)


def main():
    infile = open("fitness-data.txt","r")

    steps_total, steps_max = steps_analyzer(infile)

    heart_rate_average = heart_rate_analyzer(infile)

    sleep_total, sleep_min = sleep_analyzer(infile)
    
    outfile= open("results.txt", "a")
    outfile.write(f"The total number of steps taken this week were: {steps_total}" + "\n")

    outfile.write(f"The maximum number of steps taken this week were: {steps_max} "+ "\n")

    outfile.write(f"The average heart rate for the week was: {heart_rate_average}"+ "\n")

    outfile.write(f"The total number of hours slept this week was: {sleep_total}"+ "\n")

    outfile.write(f"The least amount of hours slept this week was: {sleep_min}"+ "\n")

    #write_results_file(results.txt)
    outfile.close()


main()
