from django.db import models
# Create your models here.


class Menu(models.Model):
    """
    菜单
    """
    title = models.CharField(max_length=32, unique=True, null=False)
    parent = models.ForeignKey("Menu", null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '菜单管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        title_list = [self.title]
        p = self.parent
        while p:
            title_list.insert(0, p.title)
            p = p.parent
        return '-'.join(title_list)


class Permission(models.Model):
    """
    权限
    """
    title = models.CharField(max_length=32, unique=True, null=False)
    url = models.CharField(max_length=128, unique=False, null=False)
    menu = models.ForeignKey("Menu", null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '权限管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{menu} --- {permission}".format(menu=self.menu, permission=self.title)


class Role(models.Model):
    """
    角色
    """
    title = models.CharField(max_length=32, unique=True)
    permissions = models.ManyToManyField("Permission")

    class Meta:
        verbose_name = '角色管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """
    用户
    """
    username = models.CharField('用户名', max_length=32, unique=True, null=False)
    password = models.CharField('密码', max_length=128, null=False)
    name = models.CharField('姓名', max_length=32, null=False)
    email = models.EmailField('邮箱', null=True)
    types = models.IntegerField('用户类型', default=False, null=False)
    database_id = models.IntegerField('数据库id', blank=False, null=False, default=1)

    roles = models.ManyToManyField("Role")

    class Meta:
        verbose_name = '用户账户管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username + " " + self.name
