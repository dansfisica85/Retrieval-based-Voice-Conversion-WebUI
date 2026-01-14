import sys
try:
    from fairseq.dataclass import configs
    print(f"Model default: {configs.FairseqConfig.__dataclass_fields__['model'].default}")
except Exception as e:
    print(f"Error: {e}")
