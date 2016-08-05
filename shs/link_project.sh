project_name=`echo $1 | gawk -F "/" '{print $(NF)}' | gawk -F "-" '{print $1}'`
# number=`echo $1 | gawk -F "/" '{print NF}'`
# echo $project_name
project_src=$1"/src/"$project_name

this_path_src=`pwd | replace "/shs" ""`
this_path_src=$this_path_src"/src"
command_src="rm -rf "$this_path_src"/"$project_name"/*"
eval $command_src
# echo $this_path
# echo $project_src
# echo $project_inc

tree -d -f -i $project_src | sed '$ d' | sed '$ d' | replace $1/src/ "" | gawk '{print "mkdir -p ../src/" $1}' > aux.sh
find $project_src -name "*.py" | replace $1/src/ "" | gawk -v ori=$1"/src" -v des=$this_path_src  '{print "ln -sf " ori "/" $1 " " des "/" $1}' >> aux.sh
chmod +x aux.sh
./aux.sh

# rm -rf ../bld/*