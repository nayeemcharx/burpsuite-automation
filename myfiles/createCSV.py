import xml.etree.ElementTree as ET
import csv
import base64

# Parse the XML file
tree = ET.parse('consolidated_items.xml')
root = tree.getroot()

# Open a CSV file to write the rows with UTF-8 encoding
with open('partTwo.csv', 'w', newline='', encoding='utf-8') as csvfile:
    # Define the CSV writer
    writer = csv.writer(csvfile)

    # Write the header row (this assumes a known structure)
    header = ['time', 'url', 'host_ip', 'host', 'port', 'protocol', 'method', 'path', 'extension', 'status', 'responselength', 'mimetype', 'request_headers', 'request_body', 'response_headers', 'response_body']
    writer.writerow(header)

    # Iterate over each item in the XML
    for item in root.findall('item'):
        row = []
        # Extract and append each field to the row
        time = item.find('time').text if item.find('time') is not None else ''
        row.append(time)
        
        url = item.find('url').text if item.find('url') is not None else ''
        row.append(url)
        
        host_ip = item.find('host').get('ip') if item.find('host') is not None else ''
        host = item.find('host').text if item.find('host') is not None else ''
        row.append(host_ip)
        row.append(host)
        
        port = item.find('port').text if item.find('port') is not None else ''
        row.append(port)
        
        protocol = item.find('protocol').text if item.find('protocol') is not None else ''
        row.append(protocol)
        
        method = item.find('method').text if item.find('method') is not None else ''
        row.append(method)
        
        path = item.find('path').text if item.find('path') is not None else ''
        row.append(path)
        
        extension = item.find('extension').text if item.find('extension') is not None else ''
        row.append(extension)
        
        status = item.find('status').text if item.find('status') is not None else ''
        row.append(status)
        
        responselength = item.find('responselength').text if item.find('responselength') is not None else ''
        row.append(responselength)
        
        mimetype = item.find('mimetype').text if item.find('mimetype') is not None else ''
        row.append(mimetype)

        # Handle the request field (decode if base64 is true)
        request_element = item.find('request')
        request_headers = ''
        request_body = ''
        if request_element is not None:
            request_base64 = request_element.get('base64') == 'true'
            request_text = request_element.text
            if request_text and request_base64:
                try:
                    request_text = base64.b64decode(request_text).decode('utf-8')
                except (UnicodeDecodeError, ValueError):
                    request_text = ''
            # Split the request into two parts using two newlines as the delimiter
            if request_text:
                parts = request_text.split('\r\n\r\n', 1)
                request_headers = parts[0] if len(parts) > 0 else ''
                request_body = parts[1] if len(parts) > 1 else ''
        row.append(request_headers)
        row.append(request_body)

        # Handle the response field (decode if base64 is true)
        response_element = item.find('response')
        response_headers = ''
        response_body = ''
        if response_element is not None:
            response_base64 = response_element.get('base64') == 'true'
            response_text = response_element.text
            if response_text and response_base64:
                try:
                    response_text = base64.b64decode(response_text).decode('utf-8')
                except (UnicodeDecodeError, ValueError):
                    response_text = ''
            # Split the response into two parts using two newlines as the delimiter
            if response_text:
                parts = response_text.split('\r\n\r\n', 1)
                response_headers = parts[0] if len(parts) > 0 else ''
                response_body = parts[1] if len(parts) > 1 else ''
        row.append(response_headers)
        row.append(response_body)

        # Write the row to the CSV
        writer.writerow(row)

print("CSV file with request and response parts has been created successfully.")
