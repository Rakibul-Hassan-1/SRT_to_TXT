from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from .forms import SRTUploadForm
from .utils import parse_srt_to_paragraph
import os

def upload_srt(request):
    if request.method == 'POST':
        form = SRTUploadForm(request.POST, request.FILES)
        if form.is_valid():
            srt_file = request.FILES['srt_file']
            srt_content = srt_file.read().decode('utf-8')
            paragraph = parse_srt_to_paragraph(srt_content)
            
            # Ensure the media directory exists
            if not os.path.exists(settings.MEDIA_ROOT):
                os.makedirs(settings.MEDIA_ROOT)
            
            # Define the output file path
            output_file_path = os.path.join(settings.MEDIA_ROOT, 'output.txt')

            # Write the paragraph to a file
            with open(output_file_path, 'w', encoding='utf-8') as f:
                f.write(paragraph)

            # Serve the file as a download
            with open(output_file_path, 'rb') as f:
                response = HttpResponse(f.read(), content_type='application/octet-stream')
                response['Content-Disposition'] = f'attachment; filename="{srt_file.name}_converted.txt"'
                return response

    else:
        form = SRTUploadForm()
    return render(request, 'upload.html', {'form': form})
