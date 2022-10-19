# recursive function for tower of hanoi.
def hanoi(disks,source,helper,destination):
    if (disks==1):
        print("Disk {} moves form tower {} to tower {} ",format(disks,source,helper,destination))