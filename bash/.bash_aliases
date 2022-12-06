mkcd ()
{
    mkdir -p -- "$1" && cd -P -- "$1"
}

# google-drive-download $filename $id
google-drive-download ()
{
    wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=$2' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=$2" -O "$1" && rm -rf /tmp/cookies.txt
}

# jupyter-env $env_name
# make sure conduct in the base env
jupyter-env ()
{
    conda install nb_conda_kernels &&
    conda activate "$1" &&
    conda install -n "$1" ipykernel &&
    python -m ipykernel install --user --name "$1"
}