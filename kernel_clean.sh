aptitude purge $(aptitude search ~ilinuximage -F %p|egrep -v "$(uname -r)|linux-imagegeneric")
