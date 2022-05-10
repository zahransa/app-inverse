
import mne
from pathlib import Path

data_path = Path(mne.datasets.sample.data_path(verbose=False))
sample_dir = data_path / 'MEG' / 'sample'
subjects_dir = data_path / 'subjects'

inverse_op_path = sample_dir / 'sample_audvis-meg-oct-6-meg-inv.fif'

report = mne.Report(title='Inverse operator example')
report.add_inverse_operator(
    inverse_operator=inverse_op_path, title='Inverse operator'
)



stc_path = sample_dir / 'sample_audvis-meg'


report.add_stc(
    stc=stc_path, subject='sample', subjects_dir=subjects_dir,
    title='Source estimate', n_time_points=2  # few for speed
)
report.save('report_inverse_sol.html', overwrite=True)