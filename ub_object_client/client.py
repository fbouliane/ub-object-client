class Client:
    # _attrs = [
    #     ('clientid', int)
    #
    # ]

    @property
    def clientid(self):
        return int(self.clientid)

    def __init__(self, clientid=None):
        self._clientid = clientid
        # self.referred_by = None
        # self.ss = None
        # self.city = None
        # self.address = None
        # self.company = None
        # self.qblistid = None
        # self.discount = None
        # self.tier_commission_rate = None
        # self.zip = None
        # self.prefer_lang = None
        # self.commission = None
        # self.cpass = None
        # self.chost = None
        # self.country = None
        # self.comments = None
        # self.salesperson = None
        # self.sales = None
        # self.discount_type = None
        # self.grace_due = None
        # self.prebill_method = None
        # self.prebill_days = None
        # self.metadata = None
        # self.tier_sales = None
        # self.commission_rate = None
        # self.class_id = None
        # self.priority = None
        # self.datesend = None
        # self.last = None
        # self.late_fee_scheme_id = None
        # self.default_renew = None
        # self.password_changed = None
        # self.latest_inv = None
        # self.charge_days = None
        # self.permnote = None
        # self.datepay = None
        # self.name_convention = None
        # self.acctmgr = None
        # self.default_billing_info = None
        # self.password_timeout = None
        # self.full_name = None
        # self.listed_company = None
        # self.commission_type = None
        # self.credit_bool = None
        # self.crv = None
        # self.fax = None
        # self.phone = None
        # self.first = None
        # self.qbeditseq = None
        # self.datedue = None
        # self.tier_commission_type = None
        # self.referred = None
        # self.retry_every = None
        # self.access = None
        # self.clogin = None
        # self.tempnote = None
        # self.clientid = None
        # self.login_enabled = None
        # self.login = None
        # self.password = None
        # self.created = None
        # self.tier_commission = None
        # self.active = None
        # self.balance = None
        # self.email = None
        # self.state = None
        # self.checkname = None
