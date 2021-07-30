from json import JSONEncoder


class Reimbursement:
    def __init__(self, reimbursement_id, reimbursement_approval, reimbursement_amount, reimbursement_reason, owner_id):
        self._reimbursement_id = reimbursement_id
        self._reimbursement_approval = reimbursement_approval
        self._reimbursement_amount = reimbursement_amount
        self._reimbursement_reason = reimbursement_reason
        self._owner_id = owner_id


class ReimbursementEncoder(JSONEncoder):
    def default(self, reimbursement):
        if isinstance(reimbursement, Reimbursement):
            return reimbursement.__dict__
        else:
            return super().default(self, reimbursement)
