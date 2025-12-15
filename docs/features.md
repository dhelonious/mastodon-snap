# 🧩 Features

## Wrapstodon

"Wrapstodon" is Mastodon's annual review of your activity. To generate it, run the command `mastodon-server.console` and paste the following script:

```
AnnualReport.prepare(2025)

User.joins(account: :account_stat)
    .confirmed
    .merge(Account.without_suspended)
    .includes(:account)
    .where(current_sign_in_at: (Date.new(2025, 1, 1)..))
    .where(account_stats: { followers_count: (1..) }).find_each do |user|
  annual_report = AnnualReport.new(user.account, 2025).generate

  next if annual_report.nil? || annual_report.data['top_statuses'].values.all?(&:nil?) || annual_report.data['top_hashtags'].empty?

  NotifyService.new.call(user.account, :annual_report, annual_report)
end
```

You need to replace the year (three occurrences) with the current year. Once the script has finished, each user will receive a notification prompting them to "View #Wrapstodon".

See this [blog post](https://blog.thms.uk/2024/12/how-to-run-wrapstodon) for further details.
