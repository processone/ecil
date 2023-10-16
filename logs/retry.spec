{groups,"/home/runner/work/ejabberd/ejabberd/test",ejabberd_SUITE,
        {mnesia,[],[{roster_master_slave,[],[{roster_subscribe,[]}]}]},
        {cases,[roster_subscribe_slave]}}.
{groups,"/home/runner/work/ejabberd/ejabberd/test",ejabberd_SUITE,
        {mnesia,[],
                [{muc_master_slave,[],[{muc_invite_password_protected,[]}]}]},
        {cases,[muc_invite_password_protected_slave]}}.
