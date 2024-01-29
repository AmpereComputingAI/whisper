import sys
import time
import torch
import whisper
import warnings
from whisper.transcribe import transcribe

warnings.filterwarnings("ignore")

#torch.jit.set_fusion_strategy([("DYNAMIC", 1)])
#model = whisper.load_model("large")
model = whisper.load_model("tiny.en")
model.eval()

#a = time.time()
with torch.no_grad():
    for _ in range(2):
        _ = transcribe(model, sys.argv[1], verbose=False)
    start = time.time()
    result = transcribe(model, sys.argv[1], verbose=False)
    finish = time.time()
    print(result["text"])
print(f"\nLatency: {round(finish-start, 2)} sec")
