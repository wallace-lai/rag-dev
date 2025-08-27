import re

def split_text_by_sentences(text, sentences_per_chunk, overlap):
    if sentences_per_chunk < 2:
        raise ValueError("一个句子至少有2个chunk")
    if overlap < 0 or overlap >= sentences_per_chunk - 1:
        raise ValueError("overlap参数必须大于等于0，且小于sentences_per_chunk")
    
    # 简化处理，用正则表达式分割句子
    sentences = re.split('(?<=[。！？])\s+', text)
    sentences = [
        sentence.strip() for sentence in sentences if sentence.strip() != ''
    ]
    if not sentences:
        print("Nothing to chunk")
        return []

    chunks = []
    i = 0
    while i < len(sentences):
        end = min(i + sentences_per_chunk, len(sentences))
        chunk = ' '.join(sentences[i : end])

        if overlap > 0 and i > 1:
            overlap_start = max(0, i - overlap)
            overlap_end = i
            overlap_chunk = ' '.join(sentences[overlap_start : overlap_end])
            chunk = overlap_chunk + ' ' + chunk
    
        chunks.append(chunk.strip())
        i += sentences_per_chunk

    return chunks

