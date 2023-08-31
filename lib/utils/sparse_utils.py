import torch


def naive_sparse_bmm(sparse_mat, dense_mat, transpose=False):
    if transpose:
        print("transpose=False")
        return torch.stack([torch.sparse.mm(s_mat, d_mat.t()) for s_mat, d_mat in zip(sparse_mat, dense_mat)], 0)
        # 把第一个维度元素相加叠
    else:
        print("transpose=True")
        return torch.stack([torch.sparse.mm(s_mat, d_mat) for s_mat, d_mat in zip(sparse_mat, dense_mat)], 0)

def sparse_permute(sparse_mat, order):
    values = sparse_mat.coalesce().values()
    indices = sparse_mat.coalesce().indices()
    indices = torch.stack([indices[o] for o in order], 0).contiguous()
    return torch.sparse_coo_tensor(indices, values)

