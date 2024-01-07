---
title: java学习
abbrlink: c2adefc4
date: 2024-01-07 21:37:30
tags:
  - java
categories:
top_img: 'linear-gradient(23deg, rgba(255, 0, 0, 0.6), rgba(0, 170, 0, 0.6), rgba(0, 0, 255, 0.6), rgba(255, 200, 0, 0.6), rgba(128, 0, 128, 0.6))'
---

## VO和DTO是什么

DTO和VO是Java中常用的数据传输对象，它们的主要区别在于它们的使用场景和目的。

DTO（Data Transfer Object）是用于在不同层之间传输数据的对象，通常用于将数据库中的数据转换为前端需要的格式，方便前后端之间的数据交互。

```java
// DTO示例
public class UserDTO {
    private String name;
    private String email;
    private String password;
    // 省略getter和setter方法
}
```

VO（Value Object）则是用于展示用的数据，不管展示方式是网页、客户端还是APP，只要是这个东西是让人看到的，这就叫VO。VO主要的存在形式就是js里面的对象（也可以简单理解成json）。

```java

// VO示例
public class UserVO {
    private String name;
    private String email;
    // 省略getter和setter方法
}

```

VO和DTO的区别主要有两个方面：一个是字段不一样，VO根据需要会删减一些字段；另一个是值不一样，VO会根据需要对DTO中的值进行展示业务的解释。在Spring Boot中，DTO和VO通常用于在Controller层和Service层之间传输数据。

下面是一个使用DTO和VO的示例：

```java
// Controller层
@RestController
@RequestMapping("/users")
public class UserController {
    @Autowired
    private UserService userService;

    @PostMapping
    public ResponseEntity<UserVO> createUser(@RequestBody UserDTO userDTO) {
        UserVO userVO = userService.createUser(userDTO);
        return ResponseEntity.ok(userVO);
    }
}

// Service层
@Service
public class UserService {
    @Autowired
    private UserRepository userRepository;

    public UserVO createUser(UserDTO userDTO) {
        User user = new User();
        user.setName(userDTO.getName());
        user.setEmail(userDTO.getEmail());
        user.setPassword(userDTO.getPassword());
        userRepository.save(user);

        UserVO userVO = new UserVO();
        userVO.setName(user.getName());
        userVO.setEmail(user.getEmail());
        return userVO;
    }
}
```

