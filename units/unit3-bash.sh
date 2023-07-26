##########################################################
### Demo code for Unit 3 of Stat243, 
### "The bash shell, UNIX utilities, and version control"
### Chris Paciorek, September 2021
##########################################################

#####################################################
# 2: Using the bash shell
#####################################################

## @knitr simple-grep-sed

grep "," file.txt  # look for lines with commas in file.txt
sed -i 's/,/;/g' file.txt  # replace commas with semicolons in file.txt

## @knitr

#####################################################
# 3: bash shell examples
#####################################################

## @knitr simple-grep-sed

grep "," file.txt  # look for lines with commas in file.txt
sed -i 's/,/;/g' file.txt  # replace commas with semicolons in file.txt

## @knitr git-clone
git clone https://github.com/berkeley-stat243/stat243-fall-2020

## @knitr data                
cd stat243-fall-2020/data
gunzip coop.txt.gz
cut -b50-70 coop.txt | less 
cut -b60-61 coop.txt | sort | uniq
cut -b60-61 coop.txt | sort | uniq -c

## @knitr mission2             
tail -n 1 cpds.csv | grep -o ',' | wc -l
nfields=$(tail -n 1 cpds.csv | grep -o ',' | wc -l)

nfields=$((${nfields}+1))
echo $nfields

## alternatively, we can use `bc`
nfields=$(echo "${nfields}+1" | bc)

## @knitr mission3
cd ../units
grep -l 'example.pdf' unit13-graphics.R
ls -tr *.R
## if unit13-graphics.R is not amongst the 5 most recently used,
## let's artificially change the timestamp so it is recently used.
touch unit13-graphics.R

ls -tr *.R | tail -n 5
ls -tr *.R | tail -n 5 | grep pdf
ls -tr *.R | tail -n 5 | grep "13-gr"
ls -tr *.R | tail -n 5 | xargs grep 'example.pdf'
ls -tr *.R | tail -n 5 | xargs grep -l 'example.pdf'
## here's how we could do it by explicitly passing the file names
## rather than using xargs
grep -l 'example.pdf' $(ls -tr *.R | tail -n 5)

## @knitr mission4

ls -rt ~/Downloads | tail -n 1

## sometimes the ~ behaves weirdly in scripting, so let's use full path 
mv "/accounts/gen/vis/paciorek/Downloads/$(ls -rt \
   /accounts/gen/vis/paciorek/Downloads | tail -n 1)" ~/Desktop

function mvlast() {
    mv "/accounts/gen/vis/paciorek/Downloads/$(ls -rt \
       /accounts/gen/vis/paciorek/Downloads | tail -n $2)" $1
}



## @knitr mission5
grep library unit[1-9]*.R
grep --no-filename library *.R
grep --no-filename "^library" *.R
grep --no-filename "^library" *.R | sort | uniq
grep --no-filename "^library" *.R | sort | uniq | cut -d'#' -f1
grep --no-filename "^library" *.R | sort | uniq | cut -d'#' -f1 | \
    tee libs.txt
grep -v "help =" libs.txt > tmp2.txt
sed 's/;/\n/g' tmp2.txt | sed 's/ //g' |
    sed 's/library(//' | sed 's/)//g' > libs.txt
## note: on a Mac, use 's/;/\\\n/g'   -- see https://superuser.com/questions/307165/newlines-in-sed-on-mac-os-x
echo "There are $(wc -l libs.txt | cut -d' ' -f1) \
unique packages we will install."
## note: on Linux, wc -l puts the number as the first characters of the output
## on a Mac, there may be a bunch of spaces preceding the number, so try this:
## echo "There are $(wc -l libs.txt | tr -s ' ' | cut -d' ' -f2) \
## unique packages we will install."


## @knitr mission5a               -
Rscript -e "pkgs <- scan('libs.txt', what = 'character'); \
install.packages(pkgs, repos = 'https://cran.r-project.org')"

## @knitr mission6             
echo "Sys.sleep(1e5)" > job.R 
nJobs=30 
for (( i=1; i<=${nJobs}; i++ )); do     
   R CMD BATCH --no-save job.R job-${i}.out & 
done 

## @knitr mission6a          
ps -o pid,pcpu,pmem,user,cmd -C R 
ps -o pid,pcpu,pmem,user,cmd,start_time --sort=start_time -C R | tail -n 30
ps -o pid --sort=start_time -C R | tail -n ${nJobs} | xargs kill

# on a Mac:
ps -o pid,pcpu,pmem,user,command | grep exec/R
# not clear how to sort by start time
ps -o pid,command | grep exec/R | cut -d' ' -f1 |  tail -n ${nJobs} | xargs kill



